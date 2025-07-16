// note: variabel
const nameTask = document.getElementById("nameTask");
const dateline = document.getElementById("dateline");
const describe = document.getElementById("describe");
const link = document.getElementById("link");


// note:detail task
const detailTask = (element) => {
  document.getElementById("detail-task").style.display = "block";
  if (element.id === "task1") {
    let tittle = "Membuat Website dengan NodeJS dan Bootstrap";
    let date = "2025-10-24: 23.59";
    let linkTask = "https://github.com";
    let describe_task =
      "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Dolore,saepe? Rerum nisi dignissimos harum, quae odit porro.";

    nameTask.textContent = tittle;
    dateline.textContent = date;
    describe.textContent = describe_task;
    link.href = linkTask;
  }
  if (element.id === "task2") {
    let tittle = "Membuat Website dengan Laravel";
    let date = "2025-10-24: 23.59";
    let linkTask = "https://youtube.com";
    let describe_task =
      "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Dolore,saepe? Rerum nisi dignissimos harum, quae odit porro.";

    nameTask.textContent = tittle;
    dateline.textContent = date;
    describe.textContent = describe_task;
    link.href = linkTask;
  }
};

// note: button back
document.querySelector(".back").addEventListener("click", () => {
  document.getElementById("detail-task").style.display = "none";
});

// note: click detail task
document.querySelectorAll(".container-task").forEach((task) => {
  task.addEventListener("click", () => {
    detailTask(task);
  });
});
