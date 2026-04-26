// 💻 Live Preview
document.getElementById("code").addEventListener("input", function () {
    const code = this.value;
    document.getElementById("preview").srcdoc = code;
});


// ⚡ Evaluate Code
async function evaluateCode() {
    const code = document.getElementById("code").value;

    document.getElementById("output").innerText = "⏳ Checking...";

    try {
        const response = await fetch("http://localhost:5000/evaluate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ code: code })
        });

        const data = await response.json();

        document.getElementById("output").innerText = data.feedback;

    } catch (error) {
        console.error("ERROR:", error);
        document.getElementById("output").innerText = "❌ Cannot connect to backend!";
    }
}