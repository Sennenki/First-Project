function clickNClose() {
    // Get the button
    let click = document.getElementById('alert');
    let count = document.querySelectorAll('.alert').length;

    for(let i = 0; i < count; i++) {
        click.style.display = "none";
    }
} 