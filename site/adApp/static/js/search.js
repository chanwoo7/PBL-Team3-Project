const search = document.querySelector('#search');

// search_ads API
search.addEventListener('click',()=>{
    let searchOpt = document.querySelector('#searchSelect');
    searchOpt = searchOpt.options[searchOpt.selectedIndex].value;
    let searchValue = document.querySelector('#searchContent').value;
    
    searchResult = requestAPI(`../api/search_ads/?ad_type=${searchOpt}&search_query=${searchValue}`,"GET");
    console.log(searchResult)
    // searchResult를 adTable.js로 보내야함
})


function requestAPI(url,met,jsonArray={}){
    const options = {
        method: met,
    };

    if (met == 'POST' || met == 'PUT') {
        options.headers = {"Content-Type": "application/json",};
        options.body = JSON.stringify(jsonArray);
    }
    

    fetch(url, options)
        .then(response => response.json())
        .then(data => {
            return data;
        })
        .catch(error => {
            console.error('Error :', error);
        });
}
