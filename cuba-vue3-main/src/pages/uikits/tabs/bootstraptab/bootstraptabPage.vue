<template>
    <breadCrumbs title="Bootstrap Tabs" main="Ui Kits" title1="Bootstrap Tabs" />
    <div class="container-fluid">
        <div class="row">
            <basicTabs/>
            <botomLeftAlign/>
            <tabsIcon/>
            <tabsRight/>
            <tabsVertical/>
            <pillsTab/>
            <pillsIcon/><pillsDark/>
            <primaryColor/><infoWarningDanger/>
        </div>
    </div>
</template>
<script>
import basicTabs from '../bootstraptab/basicTabs.vue'
import botomLeftAlign from './botomLeftAlign.vue';
import tabsIcon from './tabsIcon.vue'
import tabsRight from './tabsRight.vue'
import tabsVertical from './tabsVertical.vue'
import pillsTab from './piilsTab.vue'
import pillsIcon from './pillsIcon.vue'
import pillsDark from './pillsDark.vue'
import primaryColor from './primarySecondary.vue'
import infoWarningDanger from './infoWarningDanger.vue'
    export default{
        name: 'bootstraptabPage',
        components:{
            basicTabs,
            botomLeftAlign,tabsIcon,
            tabsRight,
            tabsVertical,pillsTab,pillsIcon,pillsDark,
            primaryColor,infoWarningDanger
        }
    }
</script>