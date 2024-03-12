<template>
  <div class="col-sm-12">
    <div class="card">
      <div class="card-header">
        <h3>Basic Table With Border Bottom Color</h3><span>Use a class<code>table</code> to any table, and <code>.border-bottom-*</code>class for Border bottom color</span>
      </div>
      <div class="table-responsive">
        <table class="table">
          <thead>
            <tr class="border-bottom-primary">
              <th scope="col">Id</th>
              <th scope="col">First Name</th>
              <th scope="col">Last Name</th>
              <th scope="col">Username</th>
              <th scope="col">Designation</th>
              <th scope="col">Company</th>
              <th scope="col">Language</th>
              <th scope="col">Country</th>
            </tr>
          </thead>
          <tbody>
            <tr class="border-bottom-secondary">
              <th scope="row">1</th>
              <td> <img class="img-30 me-2" src="@/assets/images/user/1.jpg" alt="profile">Ram Jacob</td>
              <td>Wolfe</td>
              <td>RamJacob@twitter</td>
              <td>Developer</td>
              <td>Apple Inc.</td>
              <td> <span class="badge badge-light-danger">Php</span></td>
              <td>IND</td>
            </tr>
            <tr class="border-bottom-success">
              <th scope="row">2</th>
              <td> <img class="img-30 me-2" src="@/assets/images/user/2.jpg" alt="profile">John Deo</td>
              <td>Gummer</td>
              <td>JohnDeo@twitter	</td>
              <td>Designer</td>
              <td>Hewlett packard	</td>
              <td> <span class="badge badge-light-primary">Html</span></td>
              <td>US</td>
            </tr>
            <tr class="border-bottom-info">
              <th scope="row">3</th>
              <td> <img class="img-30 me-2" src="@/assets/images/user/3.jpg" alt="profile">Elana John</td>
              <td>Cazale	</td>
              <td>ElanaJohn@twitter</td>
              <td>Designer</td>
              <td>Microsoft</td>
              <td> <span class="badge badge-light-danger">Pug</span></td>
              <td>UK</td>
            </tr>
            <tr class="border-bottom-warning">
              <th scope="row">4</th>
              <td> <img class="img-30 me-2" src="@/assets/images/user/7.jpg" alt="">Meryl Streep</td>
              <td>Roberts</td>
              <td>MerylStreep@twitter</td>
              <td>Developer</td>
              <td>Tata Ltd.	</td>
              <td> <span class="badge badge-light-success">React</span></td>
              <td>IDN</td>
            </tr>
            <tr class="border-bottom-danger">
              <th scope="row">5</th>
              <td> <img class="img-30 me-2" src="@/assets/images/user/2.png" alt="">Emma Stone</td>
              <td>Stone</td>
              <td>EmmaStone@twitter	</td>
              <td>Developer</td>
              <td>Wipro Ltd.	</td>
              <td> <span class="badge badge-light-primary">Vue</span></td>
              <td>IRN</td>
            </tr>
            <tr class="border-bottom-light"> 
              <th scope="row">6</th>
              <td> <img class="img-30 me-2" src="@/assets/images/user/3.png" alt="">Eliana Jons</td>
              <td>Jons</td>
              <td>ElianaJons@twitter		</td>
              <td>Developer</td>
              <td>Info Ltd.		</td>
              <td> <span class="badge badge-light-success">Vue</span></td>
              <td>IRN</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
  <div class="col-sm-12">
    <div class="card">
      <div class="card-header">
        <h3>Inverse Table</h3><span>Use a class <code>table-inverse</code> inside table element.</span>
      </div>
      <div class="table-responsive">
        <table class="table table-inverse">
          <thead>
            <tr class="border-bottom-light">
              <th scope="col">Id</th>
              <th scope="col">First Name</th>
              <th scope="col">Last Name</th>
              <th scope="col">Office</th>
              <th scope="col">Position</th>
              <th scope="col">Salary</th>
              <th scope="col">Join Date	</th>
              <th scope="col">Age</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th scope="row">1</th>
              <td>Stephan</td>
              <td>Laiten</td>
              <td>Tokyo</td>
              <td>Accountant</td>
              <td>$2100.00	</td>
              <td>21/01/2022		</td>
              <td>20	</td>
            </tr>
            <tr>
              <th scope="row">2</th>
              <td>Fay	</td>
              <td>Van Damme	</td>
              <td>London	</td>
              <td>CEO</td>
              <td>$1420.00		</td>
              <td>14/02/2022			</td>
              <td>22</td>
            </tr>
            <tr>
              <th scope="row">3</th>
              <td>Brevin	</td>
              <td>Oleveria</td>
              <td>New York	</td>
              <td>Software Engineer	</td>
              <td>$1340.00		</td>
              <td>04/06/2022		</td>
              <td>18	</td>
            </tr>
            <tr>
              <th scope="row">4</th>
              <td>Regina</td>
              <td>Ottandy	</td>
              <td>France	</td>
              <td>Pre-sale Support	</td>
              <td>$3400.00		</td>
              <td>10/08/2022			</td>
              <td>25	</td>
            </tr>
            <tr>
              <th scope="row">5</th>
              <td>Vani</td>
              <td>Shah	</td>
              <td>Los Angeles	</td>
              <td>Senior Developer	</td>
              <td>$3500.00	</td>
              <td>23/07/2022		</td>
              <td>28	</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
