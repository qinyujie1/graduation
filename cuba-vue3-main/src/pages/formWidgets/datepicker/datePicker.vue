<template>
  <Breadcrumbs title="Date Picker" main="Form Wizards"  />
<div class="container-fluid">
    <div class="card">
        <div class="card-header pb-0">
            <h3>Date Picker</h3>
        </div>
        <div class="card-body">
            <div class="row">
                <div class="col-md-12">
                    <div class="date-picker">
                        <form class="theme-form">
                            <div class="mb-3 row g-3">
                                <label class="col-sm-3 col-form-label text-sm-end">Default</label>
                                <div class="col-xl-5 col-sm-9">
                                    <div class="input-group">
                                        <Datepicker class="datepicker-here form-control digits" v-model="date" data-language="en"></Datepicker>
                                    </div>
                                </div>
                            </div>
                            <div class="mb-3 row g-3">
                                <label class="col-sm-3 col-form-label text-sm-end">Selecting multiple dates</label>
                                <div class="col-xl-5 col-sm-9">
                                  <Datepicker1 class="datepicker-here form-control digits" v-model="date3" multiDates />                                </div>
                            </div>
                            <div class="mb-3 row g-3">
                                <label class="col-sm-3 col-form-label text-sm-end">Month selection</label>
                                <div class="col-xl-5 col-sm-9">
                                  <Datepicker1 class="datepicker-here form-control digits" v-model="month" monthPicker range data-language="en"></Datepicker1>

                                </div>
                            </div>
                            <div class="mb-3 row g-3">
                                <label class="col-sm-3 col-form-label text-sm-end">Minimum and maximum dates</label>
                                <div class="col-xl-5 col-sm-9">
                                  <Datepicker1 class="datepicker-here form-control digits"  v-model="date4" range data-language="en"></Datepicker1>

                                </div>
                            </div>
                            <div class="mb-3 row g-3">
                                <label class="col-sm-3 col-form-label text-sm-end">Range of dates</label>
                                <div class="col-xl-5 col-sm-9">
                                  <Datepicker1 class="datepicker-here form-control digits" :multi="true" v-model="date1" range data-language="en"></Datepicker1>
                                </div>
                            </div>
                            <div class="mb-3 row g-3">
                                <label class="col-sm-3 col-form-label text-sm-end">Disable days of week</label>
                                <div class="col-xl-5 col-sm-9">
                                  <Datepicker1 class="datepicker-here form-control digits" :disabledWeekDays="[6, 0]"  v-model="date5" range data-language="en"></Datepicker1>

                                </div>
                            </div>
                            <div class="mb-3 row g-3">
                                <label class="col-sm-3 col-form-label text-sm-end">Orientation</label>
                                <div class="col-xl-5 col-sm-9">
                                    <div class="form-row">
                                        <div class="col-md-12 mb-2">
                                          <Datepicker1 class="datepicker-here form-control digits" position="left"  v-model="date6" range data-language="en"></Datepicker1>
                                        </div>
                                        <div class="col-md-12 mb-2">
                                          <Datepicker1 class="datepicker-here form-control digits" position="roght"  v-model="date7" range data-language="en"></Datepicker1>
                                        </div>
                                        <div class="col-md-12 mb-2">
                                          <Datepicker1 class="datepicker-here form-control digits" position="center"  v-model="date8" range data-language="en"></Datepicker1>
                                        </div>
                                        <div class="col-md-12">
                                          <Datepicker1 class="datepicker-here form-control digits" position="left"  v-model="date9" range data-language="en"></Datepicker1>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="mb-3 row g-3 mb-0">
                                <label class="col-sm-3 col-form-label text-sm-end">Permanently visible Datepicker</label>
                                <div class="col-sm-3">
                                  <Datepicker1 class="datepicker-here form-control digits" inline autoApply  v-model="date1" range data-language="en"></Datepicker1>

                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import Datepicker from "vue3-datepicker";

import Datepicker1 from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'
import { ref } from 'vue';
export default {
    components: {
        Datepicker,
        Datepicker1, 
    },
    data() {
        return {
            date: new Date(),
            format: 'MM/dd/yyyy',
            format2: 'MMMM yyyy',
            date4: new Date(),
            date5: new Date(),
            date6: new Date(),
            date7: new Date(),
            date8: new Date(),date9: new Date(),

            startDate: new Date(),
            endDate: new Date(),
            date1: [this.startDate, this.endDate],
            multi: true,
            month: new Date().getMonth(),
            year: new Date().getFullYear(),
            
          }},
          setup() {
        const date3 = ref();
        
        return {
          date3,
        }
    }
}
</script>
