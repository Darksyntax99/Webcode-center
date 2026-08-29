// Delete confrim
const deleteButton = document.querySelectorAll('.delete-btn');

deleteButton.forEach(function(button) {
    button.addEventListener('click', function(event) {
        const answer = confirm('Are you sure you want to delete this?');

        if (!answer) {
            event.preventDefault();
        }
    });
});
// Course search 
const searchInput = document.getElementById('course-search');
const courses = document.querySelectorAll('.course-card');

searchInput.addEventListener('keyup', function() {
    const searchText = searchInput.value.toLowerCase();
     
    courses.forEach(function(course){
        const courseName = course.textContent.toLowerCase();
    if (courseName.includes(searchText)) {
        course.style.display = '';
    } else {
        course.style.display = 'none'
    }
});
});
