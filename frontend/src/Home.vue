<template>
    <div id="home">
        <el-container>
            <el-header>
                <vheader></vheader>
            </el-header>
            <el-main><weather></weather></el-main>
            <el-footer>Footer</el-footer>
        </el-container>
    </div>
</template>

<script>
    import Header from "./components/Header";
    import Weather from "./components/Weather";

    export default {
        name: "Home",
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