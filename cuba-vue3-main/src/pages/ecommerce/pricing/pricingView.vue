<template>
<breadCrumbs title="Pricing" main="Ecommerce" title1="Pricing" />
<!-- Container-fluid starts-->
<!-- <div class="container-fluid">
    <div class="row">
        <div class="col-sm-12">
            <div class="card">
                <div class="card-header ">
                    <h5>Simple Pricing Card</h5>
                </div>
                <div class="card-body row pricing-block">
                    <div class="col-lg-3 col-md-6" v-for="(item,index) in menu" :key="index">
                        
                        <div class="card text-center pricing-simple">
                            <div class="card-body">
                                <h3>{{item.title}}</h3>
                                <h1>${{item.price}}</h1>
                                <h6 class="mb-0">{{item.text}}</h6>
                            </div><a class="btn btn-lg btn-primary btn-block" href="javascript:void(0)">
                                <h5 class="mb-0">Purchase</h5>
                            </a>
                        </div>
                    </div>
                    
                </div>
            </div>
        </div>
        <div class="col-sm-12">
            <div class="card">
                <div class="card-header pb-0">
                    <h3>Pricing</h3>
                </div>
                <div class="card-body row pricing-content pricing-col">
                    <div class="col-md-3 box-col-50" v-for="(item,index) in menu1" :key="index">
                        <div class="pricing-block card text-center" >
                            <div class="pricing-header">
                                <h2>{{item.title}}</h2>
                                <div class="price-box">
                                    <div>
                                        <h3>${{item.price}}</h3>
                                        <p>/ month</p>
                                    </div>
                                </div>
                            </div>
                            <div class="pricing-list">
                                <ul class="pricing-inner">
                                    <li>
                                        <h6>{{item.disk}}GB<span> Disk Space</span></h6>
                                    </li>
                                    <li>
                                        <h6>{{item.email}}<span> Email Accounts</span></h6>
                                    </li>
                                    <li>
                                        <h6>{{item.band}}GB<span> Bandwidth</span></h6>
                                    </li>
                                    <li>
                                        <h6>{{item.subdomain}}<span> Subdomains</span></h6>
                                    </li>
                                    <li>
                                        <h6>{{item.domain}}<span> Domains</span></h6>
                                    </li>
                                </ul>
                                <button class="btn btn-primary btn-lg" type="button" data-original-title="btn btn-primary btn-lg" title="">Subscribe</button>
                            </div>
                        </div>
                    </div>
                    
                </div>
            </div>
        </div>
    </div>
</div> -->
<!-- Container-fluid Ends-->
<div class="container-fluid">
    <div class="row">
      <div class="col-sm-12">
        <div class="card">
          <div class="card-header"> 
            <h5>Become member</h5>
          </div>
          <div class="card-body row pricing-block">
            <div class="col-lg-3 col-md-6">
              <div class="pricingtable">
                <div class="pricingtable-header">
                  <h3 class="title">Standard</h3>
                </div>
                <div class="price-value"><span class="currency">$</span><span class="amount">10</span><span class="duration">/mo</span></div>
                <ul class="pricing-content">
                  <li>50GB Disk Space</li>
                  <li>50 Email Accounts</li>
                  <li>Maintenance</li>
                  <li>15 Subdomains</li>
                </ul>
                <div class="pricingtable-signup"><a class="btn btn-primary btn-lg" href="#">Sign Up</a></div>
              </div>
            </div>
            <div class="col-lg-3 col-md-6">
              <div class="pricingtable">
                <div class="pricingtable-header">
                  <h3 class="title">Premium</h3>
                </div>
                <div class="price-value"><span class="currency">$</span><span class="amount">20</span><span class="duration">/mo</span></div>
                <ul class="pricing-content">
                  <li>10% on all product</li>
                  <li>50 Email Accounts</li>
                  <li>Maintenance</li>
                  <li>15 Subdomains</li>
                </ul>
                <div class="pricingtable-signup"><a class="btn btn-primary btn-lg" href="#">Sign Up</a></div>
              </div>
            </div>
            <div class="col-lg-3 col-md-6">
              <div class="pricingtable">
                <div class="pricingtable-header">
                  <h3 class="title">Auther pack</h3>
                </div>
                <div class="price-value"><span class="currency">$</span><span class="amount">50</span><span class="duration">/mo</span></div>
                <ul class="pricing-content">
                  <li>Upload 50 product</li>
                  <li>50 Email Accounts</li>
                  <li>Maintenance</li>
                  <li>15 Subdomains</li>
                </ul>
                <div class="pricingtable-signup"><a class="btn btn-primary btn-lg" href="#">Sign Up</a></div>
              </div>
            </div>
            <div class="col-lg-3 col-md-6">
              <div class="pricingtable">
                <div class="pricingtable-header">
                  <h3 class="title">Auther pack</h3>
                </div>
                <div class="price-value"><span class="currency">$</span><span class="amount">50</span><span class="duration">/mo</span></div>
                <ul class="pricing-content">
                  <li>Upload 50 product</li>
                  <li>50 Email Accounts</li>
                  <li>Maintenance</li>
                  <li>15 Subdomains</li>
                </ul>
                <div class="pricingtable-signup"><a class="btn btn-primary btn-lg" href="#">Sign Up</a></div>
              </div>
            </div>
          </div>
        </div>
        <div class="card">
          <div class="card-header"> 
            <h5>Simple Pricing Card</h5>
          </div>
          <div class="card-body pricing-content">
            <div class="row g-sm-4 g-3">
              <div class="col-xl-3 col-sm-6 xl-50 box-col-6">
                <div class="card text-center pricing-simple">
                  <div class="card-body">
                    <h3>Standard</h3>
                    <h1>$15</h1>
                    <h6 class="mb-0">Lorum Ipsum</h6>
                  </div><a class="btn btn-lg btn-primary btn-block" href="#">Purchase</a>
                </div>
              </div>
              <div class="col-xl-3 col-sm-6 xl-50 box-col-6">
                <div class="card text-center pricing-simple">
                  <div class="card-body">
                    <h3>Business</h3>
                    <h1>$25</h1>
                    <h6 class="mb-0">Lorum Ipsum</h6>
                  </div><a class="btn btn-lg btn-primary btn-block" href="#">Purchase</a>
                </div>
              </div>
              <div class="col-xl-3 col-sm-6 xl-50 box-col-6">
                <div class="card text-center pricing-simple">
                  <div class="card-body">
                    <h3>Premium</h3>
                    <h1>$35</h1>
                    <h6 class="mb-0">Lorum Ipsum</h6>
                  </div><a class="btn btn-lg btn-primary btn-block" href="#">Purchase</a>
                </div>
              </div>
              <div class="col-xl-3 col-sm-6 xl-50 box-col-6">
                <div class="card text-center pricing-simple">
                  <div class="card-body">
                    <h3>Extra</h3>
                    <h1>$45</h1>
                    <h6 class="mb-0">Lorum Ipsum</h6>
                  </div><a class="btn btn-lg btn-primary btn-block" href="#">Purchase</a>
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
import {data,data1} from '../../../data/pricing.json'
export default {
    name: 'pricingView',
    data(){
        return{
            menu: data,
            menu1: data1
        }
    }
}
</script>
