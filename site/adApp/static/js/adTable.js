// 전역 변수로 현재 페이지 번호를 저장하는 변수를 정의
let currentPage = 1;

// 페이지네이션 링크 클릭 이벤트 리스너를 추가하는 함수
function setupPagination() {
    const paginationLinks = document.querySelectorAll('.page-link');
    paginationLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            // data-page 속성에서 페이지 번호를 가져옴
            const page = parseInt(this.getAttribute('data-page'), 10);
            renderPage(page);
        });
    });
}

// 특정 페이지의 데이터를 렌더링하는 함수
function renderPage(page) {
    const tableBody = document.querySelector('.ad-table tbody');
    tableBody.innerHTML = '';  // 테이블 내용을 비움
    const startIndex = (page - 1) * 5;  // 페이지에 따른 시작 인덱스 계산
    const endIndex = startIndex + 5;  // 페이지에 따른 끝 인덱스 계산

    // 페이지에 해당하는 데이터로 테이블 렌더링
    for (let idx = startIndex; idx < endIndex && idx < title.length; idx++) {
        tableBody.innerHTML += `
            <tr>
                <th>${idx + 1}</th>
                <th>${title[idx]}</th>
                <th>${text[idx]}</th>
                <th>${ExposureDatetime[idx]}</th>
                <th>${count[idx]}</th>
                <th>${regdate[idx]}</th>
                <th>
                    <input type="button" class="detailO" id="detail${idx}" value="상세">
                    <input type="button" class="editO" id="edit${idx}" value="수정">
                    <input type="button" class="delO" id="del${idx}" value="삭제">
                </th>
            </tr>
        `;
    }

    // 현재 페이지 갱신
    currentPage = page;
}

// 문서 로드 시 첫 페이지 렌더링
document.addEventListener('DOMContentLoaded', () => {
    renderPage(1);  // 첫 페이지 렌더링
    setupPagination();  // 페이지네이션 이벤트 리스너 설정
});
