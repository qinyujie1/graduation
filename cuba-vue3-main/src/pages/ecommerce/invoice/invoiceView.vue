<template>
    <Breadcrumbs main="Ecommerce" title="Invoice" />
    <!-- Container-fluid starts-->
<div class="container invoice" id="print">
    <div class="row">
        <div class="col-sm-12">
            <div class="card">
                <div class="card-body">
                    <div>
                        <div>
                            <div class="row invo-header">
                                <div class="col-sm-6">
                                    <div class="d-flex align-items-center">
                                        <div class="d-flex-left"><img class="d-flex-object img-60" src="@/assets/images/other-images/logo-login.png" alt=""></div>
                                        <div class="flex-grow-1 m-l-20">
                                            <h4 class="d-flex-headin">Cuba</h4>
                                            <p>hello@cuba.in<br><span class="digits">289-335-6503</span></p>
                                        </div>
                                    </div>
                                    <!-- End Info-->
                                </div>
                                <div class="col-sm-6">
                                    <div class="text-md-end text-xs-center">
                                        <h3>Invoice #<span class="digits counter">1069</span></h3>
                                        <p>Issued: May<span class="digits"> 27, 2023</span><br> Payment Due: June <span class="digits">27, 2023</span></p>
                                    </div>
                                    <!-- End Title-->
                                </div>
                            </div>
                        </div>
                        <!-- End InvoiceTop-->
                        <hr/>
                        <div class="row invo-profile">
                            <div class="col-xl-4">
                                <div class="invo-profile-left">
                                    <div class="d-flex">
                                        <div class="d-flex-left"><img class="d-flex-object rounded-circle img-60" src="@/assets/images/user/1.jpg" alt=""></div>
                                        <div class="flex-grow-1 ms-3">
                                            <h4 class="d-flex-heading">Johan Deo</h4>
                                            <p>JohanDeo@gmail.com<br/><span class="digits">555-555-5555</span></p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-xl-8">
                                <div class="invo-profile-right">
                                    <div id="project" class="text-xl-end">
                                        <h6>Project Description</h6>
                                        <p>You're only as good as your last collection, which is an enormous pressure. Jeans represent democracy in fashion. Fashion is about dressing according to what's fashionable.</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!-- End Invoice Mid-->
                        <div>
                            <div class="table-responsive invoice-table" id="table">
                                <table class="table table-bordered table-striped">
                                    <tbody>
                                        <tr>
                                            <td class="item">
                                                <h6 class="p-2 mb-0">Item Description</h6>
                                            </td>
                                            <td class="Hours">
                                                <h6 class="p-2 mb-0">Hours</h6>
                                            </td>
                                            <td class="Rate">
                                                <h6 class="p-2 mb-0">Rate</h6>
                                            </td>
                                            <td class="subtotal">
                                                <h6 class="p-2 mb-0">Sub-total</h6>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td>
                                                <label>Brown Dress</label>
                                                <p class="m-0">aask - Brown Polyester Blend Women's Fit & Flare Dress.</p>
                                            </td>
                                            <td>
                                                <p class="itemtext digits">5</p>
                                            </td>
                                            <td>
                                                <p class="itemtext digits">$75</p>
                                            </td>
                                            <td>
                                                <p class="itemtext digits">$375</p>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td>
                                                <label>Red Shirt</label>
                                                <p class="m-0">Wild West - Red Cotton Blend Regular Fit Men's Formal Shirt.</p>
                                            </td>
                                            <td>
                                                <p class="itemtext digits">3</p>
                                            </td>
                                            <td>
                                                <p class="itemtext digits">$75</p>
                                            </td>
                                            <td>
                                                <p class="itemtext digits">$225</p>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td>
                                                <label>Flower Dress</label>
                                                <p class="m-0">Skyblue Flower Printed Sleevless Strappy Dress.</p>
                                            </td>
                                            <td>
                                                <p class="itemtext digits">10</p>
                                            </td>
                                            <td>
                                                <p class="itemtext digits">$75</p>
                                            </td>
                                            <td>
                                                <p class="itemtext digits">$750</p>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td>
                                                <label>Red Skirt</label>
                                                <p class="m-0">R L F - Red Cotton Blend Women's A-Line Skirt.</p>
                                            </td>
                                            <td>
                                                <p class="itemtext digits">10</p>
                                            </td>
                                            <td>
                                                <p class="itemtext digits">$75</p>
                                            </td>
                                            <td>
                                                <p class="itemtext digits">$750</p>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td>
                                                <p class="itemtext"></p>
                                            </td>
                                            <td>
                                                <p class="m-0">HST</p>
                                            </td>
                                            <td>
                                                <p class="m-0 digits">13%</p>
                                            </td>
                                            <td>
                                                <p class="m-0 digits">$419.25</p>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td></td>
                                            <td></td>
                                            <td class="Rate">
                                                <h6 class="mb-0 p-2">Total</h6>
                                            </td>
                                            <td class="payment digits">
                                                <h6 class="mb-0 p-2">$3,644.25</h6>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            <!-- End Table-->
                            <div class="row mt-3">
                                <div class="col-md-8">
                                    <div>
                                        <p class="legal"><strong>Thank you for your business!</strong>Payment is expected within 31 days; please process this invoice within that time. There will be a 5% interest charge per month on late invoices.</p>
                                    </div>
                                </div>
                                <div class="col-md-4">
                                    <form class="text-end invo-pal">
                                        <input type="image" :src="require('@/assets/images/other-images/paypal.png')"  alt="PayPal - The safer, easier way to pay online!">
                                    </form>
                                </div>
                            </div>
                        </div>
                        <!-- End InvoiceBot-->
                    </div>
                    <div class="col-sm-12 text-center mt-3">
                        <button class="btn btn btn-primary me-2" type="button" @click="myFunction()">Print</button>
                        <button class="btn btn-secondary" type="button">Cancel</button>
                    </div>
                    <!-- End Invoice-->
                    <!-- End Invoice Holder-->
                </div>
            </div>
        </div>
    </div>
</div>
<!-- Container-fluid Ends-->
</template>

<script>
export default {
    name: 'invoiceView',
    methods: {
        myFunction() {
            var printContents = document.getElementById('print').innerHTML;
            window.print(printContents);
        }
    }
}
</script>
