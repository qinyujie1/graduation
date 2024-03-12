<template>
<BreadCrumbs title="Job Detail" main="Job Search"  />
<div class="container-fluid">
    <div class="row">
        <jobtab />
        <div class="col-xl-9 xl-60 text-start">
            <div class="card">
                <div class="job-search">
                    <div class="card-body">
                        <div class="media"><img class="img-40 img-fluid m-r-20" :src="getImgUrl(jobs.image)" alt="">
                            <div class="media-body">
                                <h6 class="f-w-600">
                                    <router-link :to="{ name: 'jobdetails', params: { id: jobs.id }}">{{ jobs.title }}</router-link>
                                    <span class="pull-right">
                                        <router-link :to="{ name: 'jobapply', params: { id: jobs.id }}" class="btn btn-primary">Apply for this job</router-link>
                                    </span>
                                </h6>
                                <p>{{ jobs.company }} <span>{{ jobs.city }}, {{ jobs.country }} </span><span v-html="stars(jobs.stars)"></span></p>
                            </div>
                        </div>
                        <div class="job-description">
                            <h6>Job Description</h6>
                            <p v-html="jobs.description"></p>
                        </div>
                        <div class="job-description">
                            <h6>Responsibilities</h6>
                            <ul>
                                <li v-for="(r,index) in jobs.resp" :key="index" v-text="r.title"></li>
                            </ul>
                        </div>
                        <div class="job-description">
                            <h6>Requirements</h6>
                            <ul>
                                <li v-for="(rq,index) in jobs.reqs" :key="index" v-text="rq.title"></li>
                            </ul>
                        </div>
                        <div class="job-description">
                            <h6>Required Skills</h6>
                            <ul>
                                <li>Proficient understanding of web markup, including HTML5, CSS3</li>
                                <li v-for="(ski,index) in jobs.skills" :key="index" v-text="ski.title"></li>
                            </ul>
                        </div>
                        <div class="job-description">
                            <button class="btn btn-primary m-r-10" type="button"><span><i class="fa fa-check"></i></span> Save this job</button>
                            <button class="btn btn-primary " type="button"><span><i class="fa fa-share-alt"></i></span> Share</button>
                        </div>
                    </div>
                </div>
            </div>
            <div class="header-faq">
                <h6 class="mb-0 f-w-600">Similar jobs</h6>
            </div>
            <div class="row">
                <div class="col-xl-6 box-col-12 xl-100" v-for="(j,index) in jobslist" :key="index">
                    <div class="card">
                        <div class="job-search">
                            <div class="card-body">
                                <div class="media"><img class="img-40 img-fluid m-r-20" :src="getImgUrl(j.image)" alt="">
                                    <div class="media-body">
                                        <h6 class="f-w-600">
                                            <router-link :to="{ name: 'jobdetails', params: { id: j.id }}">{{ j.title }}</router-link>
                                            <span class="pull-right" v-if="j.date" v-text="j.date"></span>
                                            <span class="badge badge-primary pull-right" v-else>New</span>
                                        </h6>
                                        <p>{{ j.company }} <span>{{ j.city }}, {{ j.country }} </span><span v-html="stars(j.stars)"></span></p>
                                    </div>
                                </div>
                                <p v-html="j.description"></p>
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
import {
    mapState
} from 'vuex';
import router from '@/router';
import jobtab from "../job-list/jobTab.vue"
export default {
    components: {
        jobtab
    },
    props: ['id'],
    computed: {
        ...mapState({
            jobs: state => state.jobs.jobs.find(job => {
                if (parseInt(router.currentRoute._rawValue.params.id) === job.id)
                    return job;
            }),
            jobslist: state => state.jobs.jobs,
        })
    },
    methods: {
        getImgUrl(filename) {
            var images = require.context('../../../assets/images/job-search/', false, /\.jpg$/);
            return images('./' + filename);
        },
        stars(count) {
            var stars = '';
            for (var i = 0; i < 5; i++) {
                if (count > i) {
                    stars = stars + '<i class="fa fa-star font-warning"></i>';
                } else {
                    stars = stars + '<i class="fa fa-star font-warning-o"></i>';
                }
            }
            return stars;
        }
    }
}
</script>
