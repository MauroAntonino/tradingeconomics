var config = {
type: 'line',
data: {
    datasets: [{
    data: {{ data|safe }},
    backgroundColor: [
        '#006341'
    ],
    label: 'GDP Billions usd dolars'
    }],
    labels: {{ labels|safe }}
},
options: {
    responsive: true
}
};

window.onload = function() {
var ctx = document.getElementById('pie-chart').getContext('2d');
window.myPie = new Chart(ctx, config);
};