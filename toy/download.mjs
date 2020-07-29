let jspdf = document.createElement("script");
jspdf.onload = function () {
    let pdf = new jsPDF({ orientation: 'l', format: [1600, 900] });
    let elements = document.getElementsByTagName("img");
    let width = pdf.internal.pageSize.getWidth();
    let height = pdf.internal.pageSize.getHeight();
    for (let i in elements) {
        let img = elements[i];
        console.log("add img ", img);
        if (!/^blob:/.test(img.src)) {
            console.log("invalid src");
            continue;
        }
        let can = document.createElement('canvas');
        let con = can.getContext("2d");
        can.width = img.width;
        can.height = img.height;
        con.drawImage(img, 0, 0, img.width, img.height);
        let imgData = can.toDataURL("image/jpeg", 1.0);
        pdf.addImage(imgData, 'JPEG', 0, 0, width, height);
        pdf.addPage();
    }
    pdf.save("Exported_File.pdf");
};
jspdf.src = 'https://cdnjs.cloudflare.com/ajax/libs/jspdf/1.5.3/jspdf.debug.js';
document.body.appendChild(jspdf);