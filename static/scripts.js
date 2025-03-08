document.addEventListener('DOMContentLoaded', function () {
    const addItemButton = document.getElementById('add-item');
    const tableBody = document.getElementById('invoice-body');

    if (!addItemButton || !tableBody) {
        console.error("Add-item button or invoice-body not found.");
        return;
    }

    const staticUrl = addItemButton.getAttribute('data-static-url');

    // Function to calculate and update the total amount
    function updateTotalAmount() {
        let total = 0;
        const amountCells = tableBody.querySelectorAll('.amount');
        amountCells.forEach(cell => {
            total += parseFloat(cell.textContent) || 0;
        });

        // Find the total row (assuming it already exists in the HTML)
        const totalRow = document.getElementById('total-row');
        if (totalRow) {
            const totalAmountCell = totalRow.querySelector('.amount-total');
            if (totalAmountCell) {
                totalAmountCell.textContent = total.toFixed(2);
            }
        }
    }

    // Function to calculate amount
    function calculateAmount(row) {
        const qtyInput = row.querySelector('.qty');
        const rateInput = row.querySelector('.rate');
        const amountCell = row.querySelector('.amount');

        if (qtyInput && rateInput && amountCell) {
            const qty = parseFloat(qtyInput.value) || 0;
            const rate = parseFloat(rateInput.value) || 0;
            const amount = qty * rate;
            amountCell.textContent = amount.toFixed(2);
            updateTotalAmount(); // Update total after calculating row amount
        }
    }

    // Function to add event listeners to a row
    function addRowListeners(row) {
        const qtyInput = row.querySelector('.qty');
        const rateInput = row.querySelector('.rate');

        if (qtyInput && rateInput) {
            qtyInput.addEventListener('input', () => calculateAmount(row));
            rateInput.addEventListener('input', () => calculateAmount(row));
            calculateAmount(row); // Calculate initial amount
        }
    }

    // Add event listeners to the initial rows (if any)
    const initialRows = tableBody.querySelectorAll('tr');
    initialRows.forEach(addRowListeners);

    addItemButton.addEventListener('click', function () {
        const newRow = document.createElement('tr');
        newRow.innerHTML = `
            <td class="px-4 py-2 border"><input type="text" name="itemName" class="w-full p-1 border rounded-md" placeholder="Item Name" required></td>
            <td class="px-4 py-2 border"><input type="number" name="qty" class="w-full p-1 border rounded-md qty" value="1" required></td>
            <td class="px-4 py-2 border"><input type="number" name="rate" class="w-full p-1 border rounded-md rate" required></td>
            <td class="px-4 py-2 border"><input type="number" name="gst" class="w-full p-1 border rounded-md gst" value="18" required></td>
            <td class="px-4 py-2 border amount">0.00</td>
            <td class="px-4 py-2 border" style="text-align: center;"><button type="button" class="delete-row"><img src="${staticUrl}" alt="Delete" class="h-5 w-5"></button></td>
        `;

        tableBody.appendChild(newRow);
        addRowListeners(newRow); // Add listeners to the new row
        updateTotalAmount(); // Update total after adding a new row

        // Add delete functionality for the new row
        newRow.querySelector('.delete-row').addEventListener('click', function () {
            newRow.remove();
            updateTotalAmount(); // Update total after deleting a row
        });
    });
});