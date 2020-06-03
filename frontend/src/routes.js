/*!

=========================================================
* Material Dashboard React - v1.8.0
=========================================================

* Product Page: https://www.creative-tim.com/product/material-dashboard-react
* Copyright 2019 Creative Tim (https://www.creative-tim.com)
* Licensed under MIT (https://github.com/creativetimofficial/material-dashboard-react/blob/master/LICENSE.md)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
// @material-ui/icons
import Dashboard from "@material-ui/icons/Dashboard";
import Person from "@material-ui/icons/Person";
import DashboardPage from "views/Dashboard/Dashboard.js";
import Typography from "views/Typography/Typography.js";
import UserProfile from "views/UserProfile/UserProfile.js";
import MarketAtGlance from './views/MarketAtGlance';
import OurPortfolio from './views/OurPortfolio'

const dashboardRoutes = [
  {
    path: "/user",
    name: "Dashboard",
    icon: Person,
    component: UserProfile,
    layout: "/admin"
  },
  {
    path: "/dashboard",
    name: "Investment Details",
    icon: Dashboard,
    component: DashboardPage,
    layout: "/admin"
  },
  {
    path: "/typography",
    name: "Read More",
    icon: Dashboard,
    component: Typography,
    layout: "/admin"
  },
  {
    path: "/marketatglance",
    name: "Market At Glance",
    icon: Dashboard,
    component: MarketAtGlance,
    layout: "/admin"
  },
  {
    path: "/ourportfolio",
    name: "Our Portfolio",
    icon: Dashboard,
    component: OurPortfolio,
    layout: "/admin"
  }
];

export default dashboardRoutes;
