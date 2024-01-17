const events = [
    {id: 1, company: "현대자동차", event: "아이오닉 이벤트", dateRange: "2023 06 26 00:00:00~2023 07 01 00:00:00", count: 1000, timeStamp: "2023/05/05 12:00:00"},
    {id: 2, company: "삼성 갤럭시 100", event: "헤드기어폰 이벤트", dateRange: "2023 06 26 00:00:00~2023 07 01 00:00:00", count: 1000, timeStamp: "2023/05/05 12:02:00"},
    {id: 3, company: "노동부 일잘러", event: "일을 잘하려면 여기로..", dateRange: "2023 06 26 00:00:00~2023 07 01 00:00:00", count: 1500, timeStamp: "2023/06/01 12:00:00"},
    {id: 4, company: "피망 신규게임", event: "뉴 맞고 플러스 이벤트", dateRange: "2023 06 26 00:00:00~2023 07 01 00:00:00", count: 5000, timeStamp: "2023/06/01 12:05:00"},
    {id: 5, company: "코드스테이츠 신규강좌", event: "국민대 AD 시스템 PBL", dateRange: "2023 06 26 00:00:00~2023 07 01 00:00:00", count: 3000, timeStamp: "2023/06/10 12:00:00"},
]

function createHtmlTemplate(event) {
    return `
        <tr>
            <th>${event.id}</th>
            <th>${event.company}</th>
            <th>${event.event}</th>
            <th>${event.dateRange}</th>
            <th>${event.count}</th>
            <th>${event.timeStamp}</th>
            <th>
                <input type="button" value="상세">
                <input type="button" value="수정">
                <input type="button" value="삭제">
            </th>
        </tr>
    `;
}

// HTML 문자열 초기화
let tableHtml = '';

// 각 이벤트에 대해 반복
for (let i = 0; i < events.length; i++) {
    tableHtml += createHtmlTemplate(events[i]);
}

// DOM에 추가 (예: tbody 요소에 추가)
document.querySelector('#your-table-body').innerHTML = tableHtml;