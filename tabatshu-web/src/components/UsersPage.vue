<template>
  <div>
    <table border="1" width="100%">
      <thead>
        <tr>
          <th>User ID</th>
          <th>Password</th>
          <th>Renting</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="user in users" :key="user._id">
          <td>{{ user.userId }}</td>
          <td>{{ user.password }}</td>
          <td>{{ user.tf_rent }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      users: [], // 사용자 데이터를 저장할 배열
    };
  },
  created() {
    // REST API 호출
    this.$axios
      .get('/users') // Flask 서버에서 사용자 정보를 가져오는 API
      .then((response) => {
        this.users = response.data; // 사용자 데이터를 배열에 저장
      })
      .catch((error) => {
        console.error('Error fetching user data:', error); // 오류가 있을 경우 콘솔에 출력
      });
  },
};
</script> 

<style scoped>
.users {
  padding: 20px;
}

table {
  width: 100%;
  margin-top: 20px;
  border-collapse: collapse;
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