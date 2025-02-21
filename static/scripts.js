document.addEventListener('DOMContentLoaded', function () {
    const addItemButton = document.getElementById('add-item');
    const tableBody = document.getElementById('invoice-body');

    if (!addItemButton || !tableBody) {
        console.error("Add-item button or invoice-body not found.");
        return;
    }

    const staticUrl = addItemButton.getAttribute('data-static-url');

    addItemButton.addEventListener('click', function () {
        const newRow = document.createElement('tr');
        newRow.innerHTML = `
            <td><input type="text" name="itemName" class="w-full p-1 border rounded-md" required></td>
            <td><input type="number" name="qty" class="w-full p-1 border rounded-md qty" required></td>
            <td><input type="number" name="rate" class="w-full p-1 border rounded-md rate" required></td>
            <td><input type="number" name="gst" class="w-full p-1 border rounded-md gst" required></td>
            <td class="amount">0.00</td>
            <td>
                <button type="button" class="delete-row">
                    <img src="${staticUrl}" alt="Delete" class="h-5 w-5">
                </button>   
            </td>
        `;

        tableBody.appendChild(newRow);

        // Add delete functionality for the new row
        newRow.querySelector('.delete-row').addEventListener('click', function () {
            newRow.remove();
        });
    });
});
