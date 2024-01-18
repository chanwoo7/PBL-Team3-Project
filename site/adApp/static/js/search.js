const search = document.querySelector('#search');
// search_ads API
search.addEventListener('click',()=>{
    let searchOpt = document.querySelector('#searchSelect');
    searchOpt = searchOpt.options[searchOpt.selectedIndex].value;
    let searchValue = document.querySelector('#searchContent').value;
        
    adIdL = []
    adNameL = []
    adUrlL = []
    adStartDateL = []
    adEndDateL = []
    adPriceL = []
    advNameL = []
    adTypeL = []

    requestAPI(`../api/search_ads/?search_type=${searchOpt}&search_query=${searchValue}`,"GET")
    .then( searchResult => {
    
    // async await
    // promise
    // event-loop
    
    searchResult.forEach(ad => {
        adIdL.push(ad.id);
        adNameL.push(ad.name);
        adUrlL.push(ad.url);
        adStartDateL.push(ad.start_time);
        adEndDateL.push(ad.end_time);
        adPriceL.push(ad.ad_price);
        advNameL.push(ad.adv_name);
        adTypeL.push(ad.adTypeL)

        

        });

        reloadTable(pageNum);
    }
    
    ) ;
    
    
    
   
});


function reloadTable(pageNum){
    for (let idx=5*(pageNum-1); idx<5*pageNum; idx++){
        let isbr = idx===5*pageNum ? "" : "<br>";
    
    trTag = document.getElementById("adTable").getElementsByTagName("tr")[idx+1]
    for(let i=0; i<7; i++){
        
        trTag.getElementsByTagName("th")[0].innerHTML = adIdL[idx] ?? '-';
        trTag.getElementsByTagName("th")[1].innerHTML = adNameL[idx] ?? '-';
        trTag.getElementsByTagName("th")[2].innerHTML = adUrlL[idx] ?? '-';
        trTag.getElementsByTagName("th")[3].innerHTML = adStartDateL[idx]+' ~ '+adEndDateL[idx];
        trTag.getElementsByTagName("th")[4].innerHTML = adTypeL[idx] ?? '-';
        trTag.getElementsByTagName("th")[5].innerHTML = adPriceL[idx] ?? '-';
        trTag.getElementsByTagName("th")[6].innerHTML = advNameL[idx] ?? '-';
        trTag.getElementsByTagName("th")[7].innerHTML = `
                        <input type="button" class="detailO" id="detail${idx}" value="상세">
                        <input type="button" class="editO" id="edit${idx}"value="수정">
                        <input type="button" class="delO" id="del${idx}" value="삭제"></input>`;
       }

}
}



function requestAPI(url,met,jsonArray={}){
    const options = {
        method: met,
    };

    if (met == 'POST' || met == 'PUT') {
        options.headers = {"Content-Type": "application/json",};
        options.body = JSON.stringify(jsonArray);
    }
    
    return fetch(url, options)
        .then(response => response.json())
        .then(data => {
            return data;
        })
        .catch(error => {
            console.error('Error :', error);
        });
    
}
