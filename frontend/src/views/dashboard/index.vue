<template>
  <div class="dashboard-editor-container">
    <div class=" clearfix">
      <pan-thumb :image="avatar" style="float: left">
        Your roles:
        <span v-for="item in roles" :key="item" class="pan-info-roles">{{ item }}</span>
      </pan-thumb>
      <div class="info-container">
        <span class="display_name">Hello, {{ name }}</span>
      </div>
    </div>
    <div v-if="hasAuth('query.browse')">
      <el-row :gutter="10">
        <el-col :span="12" class="toolbar" align="right">
          <el-date-picker
            v-model="dateInput"
            align="right"
            type="date"
            placeholder="选择日期"
            value-format="timestamp"
            :picker-options="pickerOptions"
          />
        </el-col>
        <el-col :span="12" class="toolbar" align="left">
          <el-form :inline="true">
            <el-form-item>
              <!--            <el-input v-model="cityInput" placeholder="请输入城市名称" />-->
              <el-select v-model="cityInput">
                <el-option
                  v-for="item in options"
                  :key="item.value"
                  :value="item.value"
                />
              </el-select>
            </el-form-item>
            <el-form-item>
              <el-button @click="greet">export data</el-button>
            </el-form-item>
          </el-form>
        </el-col>
      </el-row>
    </div>
    <el-row align="middle">
      <el-col v-show="graphShow" :span="24" align="middle">
        <ve-line :data="temperatureData" :loading="loading" :settings="chartSettings" />
        <download-csv v-if="hasAuth('query.download')" :data="csvData">Download</download-csv>
      </el-col>

    </el-row>
    <div>
      <img :src="emptyGif" class="emptyGif">
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import PanThumb from '@/components/PanThumb'
import { fetchCityList, fetchWeather } from '@/api/weather'
import { hasAuth } from '@/utils/auth'

export default {
  name: 'DashboardEditor',
  components: { PanThumb },
  data() {
    this.chartSettings = {
      labelMap: {
        'date': '日期',
        'max': '最高温度',
        'min': '最低温度',
        'avg': '平均温度',
        'prcp': '降雨量'
      }
    }
    return {
      emptyGif: 'https://wpimg.wallstcn.com/0e03b7da-db9e-4819-ba10-9016ddfdaed3',
      cityInput: null,
      dateInput: new Date(2020, 6, 7),
      gridData: [],
      graphShow: true,
      show: false,
      loading: true,
      temperatureData: {
        columns: ['date', 'max', 'min', 'avg', 'prcp'],
        rows: []

      },
      csvData: [],
      queryData: {
        date: this.dateInput,
        city: this.cityInput
      },
      pickerOptions: {
        disabledDate(time) {
          return time.getTime() > new Date(2020, 6, 6) // js的month从0开始 什么傻逼玩意
        }
      },
      options: []

    }
  },
  computed: {
    ...mapGetters([
      'name',
      'avatar',
      'roles'
    ])
  },
  mounted() {
    console.log(this.$store.getters['hasAuth']('query.browse'))
    console.log(this.$store.getters['auth'])
    this.graphShow = false
    fetchCityList().then((res) => {
      res = res.data
      for (const item of res.city_list) {
        this.options.push({
          value: item
        })
      }
    })
  },
  methods: {
    greet: function() {
      // // let url = `http://api.openweathermap.org/data/2.5/forecast/daily?q=${this.input2}&mode=json&units=metric&cnt=7&appid=f12159c1f548ea9ab7b5ff1907b1df50`
      // let testUrl = `http://127.0.0.1:5000/api/weather?city=Beijing&date=1593835200`
      // this.loading = true;
      // this.$http.get(testUrl)
      const city = this.cityInput
      const date = (Number(this.dateInput) / 1000 | 0)
      this.$message('Data computing...')
      fetchWeather({ 'city': city, 'date': date }).then((response) => {
        console.log(response)
        response = response.data
        this.city = response.city.name
        this.gridData = response.list
        this.$message({
          message: 'Data computed!',
          type: 'success'
        })
        this.temperatureData.rows = []
        for (let i = 0; i < this.gridData.length; i++) {
          var date = new Date(this.gridData[i].dt * 1000)
          this.gridData[i].dt = `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}`
          this.gridData[i].temp.avg = (this.gridData[i].temp.max + this.gridData[i].temp.min) / 2

          this.temperatureData.rows.push({
            'date': this.gridData[i].dt,
            'max': this.gridData[i].temp.max,
            'min': this.gridData[i].temp.min,
            'avg': (this.gridData[i].temp.max + this.gridData[i].temp.min) / 2,
            'prcp': this.gridData[i].temp.prcp
          })
        }
        this.loading = false
        this.show = true
        this.graphShow = true
        this.csvData = this.temperatureData.rows
      })
        .catch(function(response) {
          console.log(response)
        })
    },
    hasAuth
  }
}
</script>

<style lang="scss" scoped>
  .emptyGif {
    display: block;
    width: 45%;
    margin: 0 auto;
  }

  .dashboard-editor-container {
    background-color: #e3e3e3;
    min-height: 100vh;
    padding: 50px 60px 0px;
    .pan-info-roles {
      font-size: 12px;
      font-weight: 700;
      color: #333;
      display: block;
    }
    .info-container {
      position: relative;
      margin-left: 190px;
      height: 150px;
      line-height: 200px;
      .display_name {
        font-size: 48px;
        line-height: 48px;
        color: #212121;
        position: absolute;
        top: 25px;
      }
    }
  }
</style>
