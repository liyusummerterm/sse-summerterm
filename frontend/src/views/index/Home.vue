<template>
  <div id="home">
    <el-container>
      <el-header>
        <vheader />
      </el-header>
      <el-main><weather /></el-main>
      <el-footer>footer</el-footer>
    </el-container>
  </div>
</template>

<script>
import Header from './components/Header'
import Weather from './components/Weather'

export default {
  name: 'Home',
  components: {
    'vheader': Header,
    'weather': Weather

  }
}
</script>

<style scoped>
    #home {
        text-align: center;
    }

</style>
