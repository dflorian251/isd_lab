const fs = require("fs");
const util = require("util");
const readFilePromise = util.promisify(fs.readFile);

async function readAndProcessFile() {
    try {
        const data = await readFilePromise('_data/publications.json');
        const fileContent = JSON.parse(data.toString());
        return fileContent; // Data available as if synchronous
    } catch (err) {
        return err;
    }
}


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



let authors_data ; // We are gonna work for now with only one author
readAndProcessFile()
    .then(data => {
        console.log("Reading successful");
        authors_data = data[0][1]; // Publications 
        stats = publsPerYear(authors_data);
        maxNumPubls = findMax(stats);
        const BAR_HEIGHT = 60; // in px
        heightPerEachPud = BAR_HEIGHT / maxNumPubls;


        // DISPLAYING THE PUDS
        let chart = document.getElementById("chart");
        var pud = document.createElement("div");
        pud.style.backgroundColor = 'blue';
        pud.style.height = heightPerEachPud;
        chart.appendChild(pud);
    })
    .catch(err => {
        console.error(err);
    });


