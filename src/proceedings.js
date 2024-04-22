
async function readAndProcessFile() {
    try {
        const data = await readFilePromise('./_data/publications.json');
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
            console.log("Reading ");
            authors_data = data[0][1]; // Publications 
            stats = publsPerYear(authors_data);
            let maxNumPubls = findMax(stats);
            console.log(maxNumPubls);
            const BAR_HEIGHT = 60; // in px
            let heightPerEachPud = BAR_HEIGHT / maxNumPubls;
            console.log(heightPerEachPud);
    
    
            // DISPLAYING THE PUDS
            let chart = document.getElementById("chart");
            var pud = document.createElement("div");
            pud.style.backgroundColor = 'blue';
            pud.style.height = heightPerEachPud;
            chart.appendChild(pud);
        })
        .catch(error => {
            console.error('Error fetching file:', error);
        });
}

fetchFileData();


