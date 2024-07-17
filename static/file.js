/*function read_file{
    let info = document.querySelector("#info");
    const fs=require('fs');
    let text= fs.readFileSync("results.csv", "utf8");
    info.textContent = text;
 }*/
// read_file();
 var data = [{
  type: "pie",
  values: [2, 3, 4, 4],
  labels: ["Wages", "Operating expenses", "Cost of sales", "Insurance"],
  textinfo: "label+percent",
  insidetextorientation: "radial"
}]

var layout = [{
  height: 700,
  width: 700
}]

Plotly.newPlot('myDiv', data, layout)