
function publsSum(yearlyPubls){
    let sum = 0;
    Object.values(yearlyPubls).forEach(year => {
        sum += year ;
    });
    return sum;
}


function publsPerYear(total_publs) {
    let yearPubls = {} ;
    total_publs.forEach(publ => {
        if (publ["year"] in yearPubls) {
            yearPubls[publ["year"]]++;
        } else {
            yearPubls[publ["year"]] = 1;
        }
    });
    return yearPubls;
}


function findMax(yearlyPubls) {
    let max = 0;
    Object.values(yearlyPubls).forEach(publsOfYear=> {
        if (publsOfYear >= max) {
            let temp = publsOfYear;
            publsOfYear = max;
            max = temp;
        }
    });
    return max;
}


// Plots the axes of the graph (that is the years of publications)
function plotAxes(stats){
    let chart = document.getElementById("chart");
    let axes = document.createElement("div");
    let axesWidth = chart.getBoundingClientRect().width ; // get the parent's width
    let divider = 1; // use to divide the bars between them, size is in px 
    let barsNum = Object.keys(stats).length;
    
    let barWidth = (axesWidth - ((barsNum - 1) * divider))/(barsNum - 1); // calculate the width of each bar
    console.log(barWidth);
    axes.style.height  = "20px";
    axes.style.backgroundColor = "grey";

    axes.innerHTML = stats.length;
    chart.appendChild(axes);
}


function plotPuds(pudHeight){
    let chart = document.getElementById("chart");
    var pud = document.createElement("div");
    pud.style.backgroundColor = 'blue';
    pud.style.height = pudHeight;
    chart.appendChild(pud);
}



function fetchFileData() {
    fetch('../../assets/publications.json')
        .then(response => {
            // Check if the request was successful
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            let authors_data, stats; // We are gonna work with one author for now
            console.log("Reading was successful!");
            authors_data = data[0][1]; // Publications 
            stats = publsPerYear(authors_data);
            

            let maxNumPubls = findMax(stats);
            const BAR_HEIGHT = 60; // in px
            let heightPerEachPud = BAR_HEIGHT / maxNumPubls;
            heightPerEachPud = `${String(heightPerEachPud)}px`
            
            
            plotPuds(heightPerEachPud);
            plotAxes(stats);
        })
        .catch(error => {
            console.error('Error fetching file:', error);
        });
}

fetchFileData();


