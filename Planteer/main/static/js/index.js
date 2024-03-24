function myconfirm() {
    if (confirm('Are You sure you want to delete?')) {
        document.getElementById("delete").click();
    } else {
        return false;
    }
}
