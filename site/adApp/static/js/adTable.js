var adIdL = ["1","245","256","590","800"]
var adNameL=["현대","삼성","노동부","피망","코드스테이츠"];
var adTextL=["아이오닉","헤드기어폰","일잘","뉴맞고","국민대AD"];
var adStartDateL = [1,2,3,4,5]
var adEndDateL = [5,4,3,3,2,1]
var countL=[1,2,3,4,5]
var regdateL=[1,2,3,4,5]

for (let idx=0; idx<5; idx++){
    let isbr = idx==7 ? "" : "<br>";

    document.write(`<tr>
                        <th>${adIdL[idx]}</th>
                        <th>${adNameL[idx]}</th>
                        <th>${adTextL[idx]}</th>
                        <th>${adStartDateL[idx]}~${adEndDateL[idx]}</th>
                        <th>${countL[idx]}</th>
                        <th>${regdateL[idx]}</th>
                        <th>
                            <input type="button" class="detailO" id="detail${idx}" value="상세">
                            <input type="button" class="editO" id="edit${idx}"value="수정">
                            <input type="button" class="delO" id="del${idx}" value="삭제">
                        </th>
                        
                    </tr>

                    


        ${isbr}`)
}