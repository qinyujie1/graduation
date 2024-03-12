import Courses from "../../data/courses.json"

const state = {
	courses : Courses.courses
};

const getters = {
	specialcourses: state =>{
		return state.courses.filter((course) => {
			if (course.special === 1)
                return course;
		});
	},
	normalcourses: state =>{
		return state.courses.filter((course) => {
			if (course.special === 0)
                return course;
		});
	}
};

export default {
	namespaced: true,
	state,
	getters,
	
};