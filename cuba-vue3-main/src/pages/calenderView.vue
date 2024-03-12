<!-- <template>
  <breadCrumbs title="Calender Basic" main="Apps" title1="Calender Basic" />
     <div class="container-fluid calendar-basic">
      <div class="row">
        <div class="col-12 text-start">
          <div class="card">
            <div class="card-body">
              <div class="col-md-12">
                <div id="right">
                  <div id="calendar">
                    <FullCalendar :options="calendarOptions" :events="events" />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  <script>
  import FullCalendar from "@fullcalendar/vue3";
  import dayGridPlugin from "@fullcalendar/daygrid";
  import interactionPlugin from "@fullcalendar/interaction";
  import timeGridPlugin from "@fullcalendar/timegrid";
  let todayStr = new Date().toISOString().replace(/T.*$/, "");
  export default {
    components: {
      FullCalendar, // make the <FullCalendar> tag available
    },
    data() {
      return {
        calendarOptions: {
          plugins: [dayGridPlugin, interactionPlugin, timeGridPlugin],
          initialView: "dayGridMonth",
          dateClick: this.handleDateClick,
          events: [
            {
              title: "All-day event",
              start: todayStr,
            },
            {
              title: "Timed event",
              start: todayStr + "T12:00:00",
            },
            { title: "event 1", date: "2022-09-01" },
            { title: "BirthDay", date: "2022-09-16" },
            { title: "All-day event", date: "2022-09-04" },
            { title: "event", date: "2022-09-20" },
          ],
          headerToolbar: {
            left: "prev,next today",
            center: "title",
            right: "dayGridMonth,timeGridWeek,timeGridDay",
          },
        },
      };
    },
  };
  </script> -->
  <template>
    <Breadcrumbs main="Apps" title="Calendar" />
     <div class="container-fluid calendar-basic">
           <div class="card">
             <div class="card-body">
               <div class="row" id="wrap">
                 <div class="col-xxl-3 box-col-30">
                   <div id="external-events">
                     <h4 class="mb-3 f-22"> Draggable Events</h4>
                     <div id="external-events-list">
                      <draggable   :group="{ name: 'universalGroup', pull: 'clone', put: false }">

                       <div class="fc-event fc-h-event fc-daygrid-event fc-daygrid-block-event btn btn-primary mb-2 w-100 text-start b-r-6">
                         <div class="fc-event-main" id="birthday"> <i class="fa fa-birthday-cake me-2"></i>Birthday Party</div>
                       </div>
                       <div class="fc-event fc-h-event fc-daygrid-event fc-daygrid-block-event btn-info btn mb-2 w-100 text-start b-r-5">
                         <div class="fc-event-main" id="meeting"> <i class="fa fa-user me-2"></i>Meeting With Team</div>
                       </div>
                       <div class="fc-event fc-h-event fc-daygrid-event fc-daygrid-block-event btn-success btn mb-2 w-100 text-start b-r-5">
                         <div class="fc-event-main" id="tour"> <i class="fa fa-plane me-2"></i>Tour & Picnic</div>
                       </div>
                       <div class="fc-event fc-h-event fc-daygrid-event fc-daygrid-block-event btn-danger btn mb-2 w-100 text-start b-r-5">
                         <div class="fc-event-main" id="reporting"> <i class="fa fa-file-text me-2"></i>Reporting Schedule</div>
                       </div>
                       <div class="fc-event fc-h-event fc-daygrid-event fc-daygrid-block-event btn-warning btn mb-2 w-100 text-start b-r-5">
                         <div class="fc-event-main" id="lunch"> <i class="fa fa-briefcase me-2"></i>Lunch & Break</div>
                       </div>
                       </draggable>
                     </div>
                     <p>
                       <input class="checkbox_animated" id="drop-remove" type="checkbox">
                       <label class="f-18" for="drop-remove">remove after drop</label>
                     </p>
                   </div>
                 </div>
                 <div class="col-xxl-9 box-col-70">
                   <div class="calendar-default" id="calendar-container">
                    <draggable :list="lista"   style="min-height: 100px" group="universalGroup">
                      <FullCalendar  id="calendar" :options="calendarOptions"  /> 
                    </draggable>
                   </div>
                 </div>
               </div>
             </div>
           </div>
     </div>
</template>
<script>
// import { Calendar } from '@fullcalendar/core';
import {
    VueDraggableNext
} from 'vue-draggable-next'
import FullCalendar from "@fullcalendar/vue3";
import dayGridPlugin from "@fullcalendar/daygrid";
import { INITIAL_EVENTS } from "@/store/modules/calendar";
import interactionPlugin from "@fullcalendar/interaction";
import timeGridPlugin from "@fullcalendar/timegrid";
import {events} from "../data/draggable"


export default {
 components: {
   FullCalendar, 
   draggable: VueDraggableNext,

 },
 data() {
   return {
     calendarOptions: {
       plugins: [dayGridPlugin, interactionPlugin, timeGridPlugin],
       initialView: "dayGridMonth",
       dateClick: this.handleDateClick,
        initialEvents: INITIAL_EVENTS, 
       editable: true,
       selectable: true,
       selectMirror: true,
       dayMaxEvents: true,
       weekends: true,
       headerToolbar: {
         left: "prev,next today",
         center: "title",
         right: "dayGridMonth,timeGridWeek,timeGridDay",
       },
     },
     lista:events,
   };
 },
};
</script>