function openReviewModal(tconst) {
    document.getElementById('reviewModal').style.display = 'block';
    document.getElementById('movieTconst').value = tconst;
}

function closeReviewModal() {
    document.getElementById('reviewModal').style.display = 'none';
}
