function generatePDF() {
    alert("print js file clicked!");
    var doc = new jsPDF();
    doc.fromHTML(document.getElementById("content"), // page element which you want to print as PDF
        15,
        15,
        {
            'width': 170
        },
        function (a) {
            doc.save("HTML2PDF.pdf");
        });
}