document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("generatorForm");
    const flipCard = document.getElementById("flipCard");
    const outputElement = document.getElementById("generatedOutput");

    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        // Get selected difficulty
        const difficulty = document.getElementById("difficulty").value;

        // Send a POST request to the server to get the generated inspiration
        const response = await fetch("/", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
            body: new URLSearchParams({ difficulty }),
        });

        if (response.ok) {
            const html = await response.text();
            const tempDiv = document.createElement("div");
            tempDiv.innerHTML = html;
            const newOutput = tempDiv.querySelector("#generatedOutput").textContent;
            
            // Update the back of the card
            outputElement.textContent = newOutput;

            // Trigger the flip animation
            flipCard.classList.add("flip");

            // Reset the card flip after 2 seconds for reuse
            setTimeout(() => {
                flipCard.classList.remove("flip");
            }, 2000);
        }
    });
});
