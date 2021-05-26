<template>
	<div>
		<Navbar />
		<Nuxt />
		<Footer />
	</div>
</template>

<script>
import Footer from "@/components/layout/Footer";
import Navbar from "@/components/layout/Navbar";

export default {
	components: {
		Footer,
		Navbar,
	},
};
</script>
