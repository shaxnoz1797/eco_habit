document.addEventListener("DOMContentLoaded", function () {

    console.log("JS IS WORKING 🔥");

    function loadProgress() {
        fetch("/progress/")
            .then(res => res.json())
            .then(data => {
                document.getElementById("progress-bar").style.width = data.percent + "%";
                document.getElementById("progress-text").innerText =
                    `Progress: ${data.percent}% (${data.done}/${data.total})`;
            });
    }

    loadProgress();

    document.querySelectorAll(".toggle-btn").forEach(button => {
        button.addEventListener("click", function () {

            const card = this.closest(".card");
            const id = card.getAttribute("data-id");

            console.log("CLICKED ID:", id);

            fetch(`/toggle-habit/${id}/`)
                .then(res => res.json())
                .then(data => {

                    const status = card.querySelector(".status");

                    if (data.is_done) {
                        status.innerHTML = `<span class="done-text">Completed ✅</span>`;
                        this.innerHTML = "Undo ❌";
                    } else {
                        status.innerHTML = `<span class="pending-text">Pending ⏳</span>`;
                        this.innerHTML = "Done ✅";
                    }

                    loadProgress();
                });
        });
    });

});