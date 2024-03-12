<template>
    <Breadcrumbs title="Creative Card" main="Card"  />
    <div class="container-fluid">
        <div class="row">
          <div class="col-sm-12">
            <div class="card">
              <div class="card-header pb-0">
                <h3>Single File Upload</h3>
              </div>
              <div class="card-body">
                <form class="dropzone" id="singleFileUpload" action="/upload.php">
                  <div class="dz-message needsclick"><i class="icon-cloud-up"></i>
                    <DropZone :maxFileSize="Number(60000000)" url="http://localhost:8080" :uploadOnDrop="true"  />
                </div>
                </form>
              </div>
            </div>
          </div>
          <div class="col-sm-12">
            <div class="card">
              <div class="card-header pb-0">
                <h3>Multi File Upload</h3>
              </div>
              <div class="card-body">
                <form class="dropzone dropzone-primary" id="multiFileUpload" action="/upload.php">
                  <div class="dz-message needsclick"><i class="icon-cloud-up"></i>
                    <DropZone :maxFileSize="Number(60000000)" url="http://localhost:8080" :uploadOnDrop="true" :multipleUpload="true" :parallelUpload="2" />
                </div>
                </form>
              </div>
            </div>
          </div>
          <!-- <div class="col-sm-12">
            <div class="card">
              <div class="card-header pb-0">
                <DropZone :maxFileSize="Number(60000000)" url="http://localhost:8080" :uploadOnDrop="true" :multipleUpload="true" :parallelUpload="2" />
            </div>
              <div class="card-body">
                <form class="dropzone dropzone-info" id="fileTypeValidation" action="/upload.php">
                  <div class="dz-message needsclick">
                    <h4>Drop files here or click to upload.</h4><span class="note needsclick">(This is just a demo dropzone. Selected files are <strong>not</strong> actually uploaded.)</span>
                  </div>
                </form>
              </div>
            </div>
          </div> -->
          <div class="col-sm-12">
            <div class="card">
              <div class="card-header">
                <h5>File Type Validation</h5>
              </div>
              <div class="card-body">
                <form class="dropzone dropzone-info" id="fileTypeValidation" action="/upload.php">
                  <div class="dz-message needsclick"><i class="icon-cloud-up"></i>
                    <DropZone :maxFileSize="Number(60000000)" url="http://localhost:8080" :uploadOnDrop="true" :multipleUpload="true" :parallelUpload="2" />
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
</template>