let title=["현대","삼성","노동부","피망","코드스테이츠"];
let text=["아이오닉","헤드기어폰","일잘","뉴맞고","국민대AD"];
let ExposureDatetime=["1~2","2~3","3~4","4~5","5~6"];
let count=[1,2,3,4,5]
let regdate=[1,2,3,4,5]

for (let idx=0; idx<5; idx++){
    let isbr = idx==7 ? "" : "<br>";

    document.write(`<tr>
                        <th>${idx}</th>
                        <th>${title[idx]}</th>
                        <th>${text[idx]}</th>
                        <th>${ExposureDatetime[idx]}</th>
                        <th>${count[idx]}</th>
                        <th>${regdate[idx]}</th>
                        <th>
                            <input type="button" class="detail" id="detail${idx}" value="상세">
                            <input type="button" class="edit" id="edit${idx}"value="수정">
                            <input type="button" class="del" id="del${idx}" value="삭제">
                        </th>
    </tr>${isbr}`)
}