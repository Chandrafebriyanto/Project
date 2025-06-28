// note: click task
const detailTask = () =>{
    document.getElementById('detail-task').style.display = 'block';
}

// note: button back
document.querySelector('.back').addEventListener('click', () => {
    document.getElementById('detail-task').style.display = 'none';
})

