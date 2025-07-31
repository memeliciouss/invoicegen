// myapp/static/script.js

// This script handles dynamic adding, removing, re-indexing, and total calculation
// for item rows in both invoice creation and editing forms.

// The values for FORMSET_PREFIX and IS_EDIT_PAGE are set in a small
// inline script in the HTML template before this file is loaded.

document.addEventListener('DOMContentLoaded', function() {
    // Access the global variables defined in the HTML template
    const prefix = typeof FORMSET_PREFIX !== 'undefined' ? FORMSET_PREFIX : 'items';
    const isEditPage = typeof IS_EDIT_PAGE !== 'undefined' ? IS_EDIT_PAGE : false;

    // Get references to key HTML elements by their new, consistent IDs and classes
    const addItemButton = document.getElementById('add-item-button');
    const itemTableBody = document.querySelector('#item-table tbody');
    const emptyFormTemplate = document.getElementById('empty-form-template');
    
    // Get the hidden management form input for TOTAL_FORMS
    const totalFormsInput = document.querySelector('input[name$="TOTAL_FORMS"][type="hidden"]');

    // Get references to display elements for calculated totals
    const subtotalDisplay = document.getElementById('subtotal-display');
    const gstTotalDisplay = document.getElementById('gst-total-display');
    const grandTotalDisplay = document.getElementById('grand-total-display');

    /**
     * Updates the 'name', 'id', and 'for' attributes of an element
     * to match the new form index. This is crucial for Django formsets.
     * @param {HTMLElement} element The HTML element (input, label, select, textarea) to update.
     * @param {number} index The new numerical index for the form (e.g., 0, 1, 2...).
     */
    function updateElementIndex(element, index) {
        const oldPrefixPlaceholder = `${prefix}-__prefix__`;
        const newPrefix = `${prefix}-${index}`;
        
        if (element.name) {
            element.name = element.name.replace(oldPrefixPlaceholder, newPrefix);
        }
        if (element.id) {
            element.id = element.id.replace(oldPrefixPlaceholder, newPrefix);
        }
        if (element.labels) {
            for (const label of element.labels) {
                if (label.htmlFor) {
                    label.htmlFor = label.htmlFor.replace(oldPrefixPlaceholder, newPrefix);
                }
            }
        } else if (element.htmlFor) {
            element.htmlFor = element.htmlFor.replace(oldPrefixPlaceholder, newPrefix);
        }
    }

    /**
     * Calculates and updates the displayed subtotal, GST total, and grand total.
     * It intelligently skips rows that are marked for deletion (only on edit page).
     */
    function calculateTotals() {
        let currentSubtotal = 0;
        let currentGstTotal = 0;

        itemTableBody.querySelectorAll('tr.item-row').forEach(function(row) {
            if (row.id === 'empty-form-template') {
                return;
            }

            if (isEditPage) {
                const deleteInput = row.querySelector('input[name$="-DELETE"][type="hidden"]');
                const isExistingItem = row.querySelector('input[name$="-id"][type="hidden"]'); 
                
                if (isExistingItem && deleteInput && (deleteInput.value === 'on' || deleteInput.value === 'True')) {
                    return;
                }
            }

            const rateInput = row.querySelector('[name$="-rate"]');
            const gstInput = row.querySelector('[name$="-gst"]');
            const qtyInput = row.querySelector('[name$="-qty"]');

            const rate = parseFloat(rateInput ? rateInput.value || 0 : 0);
            const gst = parseFloat(gstInput ? gstInput.value || 0 : 0);
            const qty = parseFloat(qtyInput ? qtyInput.value || 0 : 0);

            if (!isNaN(rate) && !isNaN(gst) && !isNaN(qty)) {
                const itemAmount = rate * qty;
                const itemGstAmount = itemAmount * (gst / 100);

                currentSubtotal += itemAmount;
                currentGstTotal += itemGstAmount;
            }
        });

        const currentGrandTotal = currentSubtotal + currentGstTotal;

        if (subtotalDisplay) subtotalDisplay.textContent = currentSubtotal.toFixed(2);
        if (gstTotalDisplay) gstTotalDisplay.textContent = currentGstTotal.toFixed(2);
        if (grandTotalDisplay) grandTotalDisplay.textContent = currentGrandTotal.toFixed(2);
    }

    /**
     * Attaches a click listener to a "Remove" button.
     * The behavior depends on whether it's an edit page (mark for deletion) or generate page (remove from DOM).
     * @param {HTMLElement} button The "Remove" button element.
     */
    function addRemoveButtonListener(button) {
        button.addEventListener('click', function() {
            const row = this.closest('tr.item-row');
            if (row) {
                if (isEditPage) {
                    const deleteInput = row.querySelector('input[name$="-DELETE"][type="hidden"]');
                    const isExistingItem = row.querySelector('input[name$="-id"][type="hidden"]');

                    if (isExistingItem && deleteInput) {
                        deleteInput.value = 'on';
                        row.style.display = 'none';
                    } else {
                        row.remove();
                        let totalForms = parseInt(totalFormsInput.value);
                        totalForms--;
                        totalFormsInput.value = totalForms;
                    }
                } else {
                    row.remove();
                    let totalForms = parseInt(totalFormsInput.value);
                    totalForms--;
                    totalFormsInput.value = totalForms;
                }
                reindexRows();
                calculateTotals();
            }
        });
    }

    /**
     * Re-indexes the 'name', 'id', and 'for' attributes of all visible form elements.
     */
    function reindexRows() {
        const rows = itemTableBody.querySelectorAll('tr.item-row:not([style*="display: none"]):not(#empty-form-template)');
        rows.forEach((row, index) => {
            row.querySelectorAll('input, select, textarea, label').forEach(element => {
                updateElementIndex(element, index);
            });
        });
    }

    // --- Initial Setup ---
    document.querySelectorAll('.remove-row-button').forEach(button => {
        addRemoveButtonListener(button);
    });

    addItemButton.addEventListener('click', function() {
        const newRow = emptyFormTemplate.cloneNode(true);
        newRow.removeAttribute('id');
        newRow.style.display = '';
        newRow.classList.add('item-row');

        let totalForms = parseInt(totalFormsInput.value);

        newRow.querySelectorAll('input, select, textarea, label').forEach(element => {
            updateElementIndex(element, totalForms);
            if (element.tagName === 'INPUT' || element.tagName === 'SELECT' || element.tagName === 'TEXTAREA') {
                element.value = '';
                element.checked = false;
            }
            if (element.name && (element.name.endsWith('-rate') || element.name.endsWith('-gst') || element.name.endsWith('-qty'))) {
                element.addEventListener('input', calculateTotals);
            }
        });

        const newRemoveButton = newRow.querySelector('.remove-row-button');
        if (newRemoveButton) {
            addRemoveButtonListener(newRemoveButton);
        }

        itemTableBody.appendChild(newRow);

        totalForms++;
        totalFormsInput.value = totalForms;
        
        calculateTotals();
    });

    itemTableBody.querySelectorAll('tr.item-row input[name$="-rate"], tr.item-row input[name$="-gst"], tr.item-row input[name$="-qty"]').forEach(function(input) {
        input.addEventListener('input', calculateTotals);
    });

    calculateTotals();
});
