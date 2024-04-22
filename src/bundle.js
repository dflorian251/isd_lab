(function(){function r(e,n,t){function o(i,f){if(!n[i]){if(!e[i]){var c="function"==typeof require&&require;if(!f&&c)return c(i,!0);if(u)return u(i,!0);var a=new Error("Cannot find module '"+i+"'");throw a.code="MODULE_NOT_FOUND",a}var p=n[i]={exports:{}};e[i][0].call(p.exports,function(r){var n=e[i][1][r];return o(n||r)},p,p.exports,r,e,n,t)}return n[i].exports}for(var u="function"==typeof require&&require,i=0;i<t.length;i++)o(t[i]);return o}return r})()({1:[function(require,module,exports){

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



// let authors_data ; // We are gonna work for now with only one author
// await readAndProcessFile()
//     .then(data => {
//         console.log("Reading successful");
//         authors_data = data[0][1]; // Publications 
//         stats = publsPerYear(authors_data);
//         maxNumPubls = findMax(stats);
//         const BAR_HEIGHT = 60; // in px
//         heightPerEachPud = BAR_HEIGHT / maxNumPubls;


//         // DISPLAYING THE PUDS
//         let chart = document.getElementById("chart");
//         var pud = document.createElement("div");
//         pud.style.backgroundColor = 'blue';
//         pud.style.height = heightPerEachPud;
//         chart.appendChild(pud);
//     })
//     .catch(err => {
//         console.error(err);
//     });

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
            console.log('File data:', data);
        })
        .catch(error => {
            console.error('Error fetching file:', error);
        });
}

fetchFileData();



},{}]},{},[1]);
