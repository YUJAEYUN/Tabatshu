<template>
  <div>
    <table border="1" width="100%">
      <thead>
        <tr>
          <th>Bike ID</th>
          <th>User ID</th>
          <th>Category</th>
          <th>Contents</th>
          <th>Image</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="report in reports" :key="report._id">
          <td>{{ report.bikeId }}</td>
          <td>{{ report.userId }}</td>
          <td>{{ report.category }}</td>
          <td>{{ report.contents }}</td>
          <td>
            <img 
  v-if="report.imageId" 
  :src="'http://127.0.0.1:5000/reports/image/' + report.imageId" 
  alt="Report Image" 
  width="100" 
/>

          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      reports: [], // 신고 데이터를 저장할 배열
    };
  },
  created() {
    // REST API 호출
    this.$axios
      .get('/reports') // Flask 서버에서 신고 데이터를 가져오는 API
      .then((response) => {
        this.reports = response.data; // 가져온 데이터를 reports 배열에 저장
      })
      .catch((error) => {
        console.error('Error fetching reports data:', error); // 오류 출력
      });
  },
};
</script>

<style>
.reports {
  padding: 20px;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

th, td {
  padding: 10px;
  text-align: center;
}

th {
  background-color: #f5a55b;
  color : white;
  font-size: 20px;
}

tbody tr:nth-child(even) {
  background-color: #f9f9f9;
}

.reports-image {
  max-width: 100px;
  max-height: 100px;
  object-fit: cover;
}

@keyframes fadeInOut {
  0% {
    opacity: 0;
  }
  10% {
    opacity: 1;
  }
  90% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}
</style>