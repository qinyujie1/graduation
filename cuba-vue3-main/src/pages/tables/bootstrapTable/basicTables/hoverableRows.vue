<template>
  <div class="col-sm-12">
    <div class="card">
      <div class="card-header">
        <h3>Caption</h3><span>A <code>&lt;caption&gt;</code> functions like a heading for a table. It helps users with screen readers to find a table and understand what it’s about and decide if they want to read it.</span>
      </div>
      <div class="card-block row">
        <div class="col-sm-12 col-lg-12 col-xl-12">
          <div class="table-responsive">
            <table class="table">
              <caption>List of users</caption>
              <thead>
                <tr>
                  <th scope="col">Id</th>
                  <th scope="col">Employee Name	</th>
                  <th scope="col">Email</th>
                  <th scope="col">Experience</th>
                  <th scope="col">Sex</th>
                  <th scope="col">Contact No.	</th>
                  <th scope="col">Age</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <th scope="row">1</th>
                  <td>Elana Robbert	</td>
                  <td>ElanaRob@gmail.com	</td>
                  <td>1 Year	</td>
                  <td>Male	</td>
                  <td>+91 9789887777		</td>
                  <td>28	</td>
                </tr>
                <tr>
                  <th scope="row">2</th>
                  <td>Stiphen Deo		</td>
                  <td>Stiphen@yahoo.com		</td>
                  <td>6 Month		</td>
                  <td>Female</td>
                  <td>+91 9874563210		</td>
                  <td>22	</td>
                </tr>
                <tr>
                  <th scope="row">3</th>
                  <td>Genelia Ottre	</td>
                  <td>Genelia@gmail.com	</td>
                  <td>2 Days		</td>
                  <td>Male	</td>
                  <td>+91 8794562135		</td>
                  <td>24	</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="col-sm-6"> 
    <div class="card">
      <div class="card-header">
        <h3>Table head options</h3><span>Similar to tables , use the modifier classes<code>.table-[color]</code>  to make <code>thead</code>appear in any color.</span>
      </div>
      <div class="card-block row">
        <div class="col-sm-12 col-lg-12 col-xl-12">
          <div class="table-responsive">
            <table class="table">
              <thead class="table-dark">
                <tr>
                  <th scope="col">Id</th>
                  <th scope="col">First Name</th>
                  <th scope="col">Last Name</th>
                  <th scope="col">Username</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <th scope="row">1</th>
                  <td>Mark</td>
                  <td>Otto</td>
                  <td>@mdo</td>
                </tr>
                <tr>
                  <th scope="row">2</th>
                  <td>Jacob</td>
                  <td>Thornton</td>
                  <td>@fat</td>
                </tr>
                <tr>
                  <th scope="row">3</th>
                  <td>Larry</td>
                  <td>the Bird</td>
                  <td>@twitter</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
