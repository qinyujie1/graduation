<template>
    <Breadcrumbs title="Time Picker" main="Form Wizards" />
    <div class="container-fluid">
        <div class="card">
          <div class="card-header pb-0">
            <h3>Date Range Picker</h3>
          </div>
          <div class="card-body">
            <div class="row date-range-picker">
              <div class="col-xl-6">
                <h4 class="sub-title">Date Range Picker</h4>
                <p>The Date Range Picker use the current value of the input to initialize, and update the input if new dates are chosen.</p>
                <div class="theme-form">
                  <div>
                    <Datepicker1 class="datepicker-here form-control digits" v-model="date3" range multiCalendars /> 
                  </div>
                </div>
              </div>
              <div class="col-xl-6">
                <h4 class="sub-title">Predefined Ranges</h4>
                <p>This example shows the option to predefine date ranges that the user can choose from a list.</p>
                <div class="theme-form">
                  <div>
                    <Datepicker1 class="datepicker-here form-control digits" v-model="date3" range :presetRanges="presetRanges">
                    <template #yearly="{ label, range, presetDateRange }">
                        <span @click="presetDateRange(range)">{{ label }}</span>
                      </template> 
                    </Datepicker1>
                  </div>
                </div>
              </div>
              <div class="col-xl-6">
                <h4 class="sub-title">Single Date Picker</h4>
                <p>The Date Range Picker can be turned into a single date picker widget with only one calendar. In this example, dropdowns to select a month and year have also been enabled at the top of the calendar to quickly jump to different months.</p>
                <div class="theme-form">
                  <div>
                    <Datepicker1 class="datepicker-here form-control digits" v-model="date3" @click.prevent="birthday()" /> 

                  </div>
                </div>
              </div>
              <div class="col-xl-6">
                <h4 class="sub-title">Input Initially Empty</h4>
                <p>If you're using a date range as a filter, you may want to attach a picker to an input but leave it empty by default. This example shows how to accomplish that using the <code>autoUpdateInput</code> setting, and the <code>apply</code> and <code>cancel</code> events.</p>
                <div class="theme-form">
                  <div>
                    <Datepicker1 class="datepicker-here form-control digits" v-model="date3" range multiCalendars /> 
                  </div>
                </div>
              </div>
              <div class="col-lg-12">
                <h4 class="sub-title">Date and Time</h4>
                <p>The Date Range Picker can also be used to select times. Hour, minute and (optional) second dropdowns are added below the calendars. An option exists to set the increment count of the minutes dropdown to e.g. offer only 15-minute or 30-minute increments.</p>
                <div class="theme-form">
                  <div>
                    <Datepicker1 class="datepicker-here form-control digits" v-model="date3" range multiCalendars /> 
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
</template>
<script>
import Datepicker1 from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'
import { endOfMonth, endOfYear, startOfMonth, startOfYear, subMonths } from 'date-fns';
export default{
    components: {
       
        Datepicker1, 
    },
    data() {
        return {
           
            
            date3: new Date(),
            date5: new Date(),
            date1: new Date(),
            time :[{ 
            hours: new Date().getHours(),
            minutes: new Date().getMinutes()
        }],
        date:new Date().toLocaleDateString(),
        presetRanges : [
          { label: 'Today', range: [new Date(), new Date()] },
          { label: 'This month', range: [startOfMonth(new Date()), endOfMonth(new Date())] },
          {
            label: 'Last month',
            range: [startOfMonth(subMonths(new Date(), 1)), endOfMonth(subMonths(new Date(), 1))],
          },
          { label: 'This year', range: [startOfYear(new Date()), endOfYear(new Date())] },
          {
            label: 'This year (slot)',
            range: [startOfYear(new Date()), endOfYear(new Date())],
            slot: 'yearly',
          },
        ]
    
}
},

}
</script>