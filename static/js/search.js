document.addEventListener('DOMContentLoaded', function () {
//    var form = document.querySelector('.box5 form');
    var form = document.querySelector('#form1');

    document.getElementById('searchByDocBtn').addEventListener('click', function(event) {
        event.preventDefault();
        form.action = this.getAttribute('data-action');
        form.submit();
    });

    document.getElementById('searchByAuthorBtn').addEventListener('click', function(event) {
        event.preventDefault();
        form.action = this.getAttribute('data-action');
        form.submit();
    });
});
