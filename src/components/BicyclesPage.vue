<template>
  <div>
    <table border="1" width="100%">
      <thead>
        <tr>
          <th>Bike ID</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="bicycle in bicycles" :key="bicycle._id">
          <td>{{ bicycle.bikeId }}</td>
          <td>{{ bicycle.status }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      bicycles: [], // 자전거 데이터를 저장할 배열
    };
  },
  created() {
    // REST API 호출
    this.$axios
      .get('/bicycles') // Flask 서버에서 자전거 데이터를 가져오는 API
      .then((response) => {
        this.bicycles = response.data; // 가져온 데이터를 bicycles 배열에 저장
      })
      .catch((error) => {
        console.error('Error fetching bicycle data:', error); // 오류 출력
      });
  },
};
</script>

<style scoped>
.bicycles {
  padding: 20px;
}

table {
  width: 100%;
  margin-top: 20px;
  border-collapse: collapse;
  border-radius: 30px;
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

</style>