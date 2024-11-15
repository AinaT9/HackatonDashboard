function changeDevice(deviceName) {
    // Cambiar el texto del botón con el nombre del dispositivo seleccionado
    document.getElementById("dropdownMenuButton").innerText = deviceName;

    // Recargar la página para aplicar los cambios
    location.reload();
}