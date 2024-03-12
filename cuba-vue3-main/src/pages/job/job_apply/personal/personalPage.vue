<template>
    <h6 class="mb-0">Personal Details</h6>
										<form class="form theme-form">
											<div class="row">
												<div class="col">
													<div class="form-group">
														<label for="exampleFormControlInput1">First Name:<span class="font-danger">*</span></label>
														<input class="form-control" id="exampleFormControlInput1" type="email" placeholder="Enter first name">
													</div>
												</div>
											</div>
											<div class="row">
												<div class="col">
													<div class="form-group">
														<label for="exampleFormControlInput2">Last Name:<span class="font-danger">*</span></label>
														<input class="form-control" id="exampleFormControlInput2" type="email" placeholder="Enter last name">
													</div>
												</div>
											</div>
											<div class="row">
												<div class="col">
													<div class="form-group">
														<label for="exampleFormControlInput3">Email:<span class="font-danger">*</span></label>
														<input class="form-control" id="exampleFormControlInput3" type="email" placeholder="Enter email">
													</div>
												</div>
											</div>
											<div class="row">
												<div class="col">
													<div class="form-group">
														<label for="exampleFormControlpassword">Password:<span class="font-danger">*</span></label>
														<input class="form-control" id="exampleFormControlpassword" type="password" placeholder="Enter password">
													</div>
												</div>
											</div>
											<div class="row">
												<div class="col">
													<div class="form-group">
														<label for="exampleFormControlpassword1">Repeat Password:<span class="font-danger">*</span></label>
														<input class="form-control" id="exampleFormControlpassword1" type="password" placeholder="Repeat password">
													</div>
												</div>
											</div>
											<div class="row birthday-select">
												<birthdayselect/>
											</div>
										</form>
</template>
<script>
import birthdayselect from "./birthdaySelect.vue"
export default {
	components:{
      birthdayselect
	}
}
</script>