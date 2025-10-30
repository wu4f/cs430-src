output "instance_nat_ips" {
  value = {
    w1   = try(google_compute_instance.w1_vm.network_interface[0].access_config[0].nat_ip, null),
    w2   = try(google_compute_instance.w2_vm.network_interface[0].access_config[0].nat_ip, null),
    e1   = try(google_compute_instance.e1_vm.network_interface[0].access_config[0].nat_ip, null),
    eu1  = try(google_compute_instance.eu1_vm.network_interface[0].access_config[0].nat_ip, null),
    asia1= try(google_compute_instance.asia1_vm.network_interface[0].access_config[0].nat_ip, null),
  }
}

output "instance_internal_ips" {
  value = {
    w1   = google_compute_instance.w1_vm.network_interface[0].network_ip,
    w2   = google_compute_instance.w2_vm.network_interface[0].network_ip,
    e1   = google_compute_instance.e1_vm.network_interface[0].network_ip,
    eu1  = google_compute_instance.eu1_vm.network_interface[0].network_ip,
    asia1= google_compute_instance.asia1_vm.network_interface[0].network_ip,
  }
}
