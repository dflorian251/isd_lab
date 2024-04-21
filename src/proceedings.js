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


let authors_data ; // We are gonna work for now with only one author
readAndProcessFile()
    .then(data => {
        console.log("Reading successful");
        authors_data = data[0][1]; // Publications 
        console.log(publsSum(publsPerYear(authors_data)));
        
    })
    .catch(err => {
        console.error(err);
    });


