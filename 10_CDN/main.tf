terraform {
  required_version = ">= 1.5.0"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.40"
    }
  }
}

provider "google" {
 credentials = file("CDN-lab.json")
 project = var.project_id
}

# --------------------
# Network
# --------------------
resource "google_compute_network" "networking101" {
  name                    = var.network_name
  auto_create_subnetworks = false
}

# --------------------
# Subnetworks
# --------------------
resource "google_compute_subnetwork" "us_west_s1" {
  name          = "us-west-s1"
  region        = "us-west1"
  ip_cidr_range = "10.10.0.0/16"
  network       = google_compute_network.networking101.self_link
  private_ip_google_access = true
}

resource "google_compute_subnetwork" "us_west_s2" {
  name          = "us-west-s2"
  region        = "us-west1"
  ip_cidr_range = "10.11.0.0/16"
  network       = google_compute_network.networking101.self_link
  private_ip_google_access = true
}

resource "google_compute_subnetwork" "us_east5" {
  name          = "us-east5"
  region        = "us-east5"
  ip_cidr_range = "10.20.0.0/16"
  network       = google_compute_network.networking101.self_link
  private_ip_google_access = true
}

resource "google_compute_subnetwork" "europe_west1" {
  name          = "europe-west1"
  region        = "europe-west1"
  ip_cidr_range = "10.30.0.0/16"
  network       = google_compute_network.networking101.self_link
  private_ip_google_access = true
}

resource "google_compute_subnetwork" "asia_east1" {
  name          = "asia-east1"
  region        = "asia-east1"
  ip_cidr_range = "10.40.0.0/16"
  network       = google_compute_network.networking101.self_link
  private_ip_google_access = true
}

# --------------------
# Instances
# --------------------
data "google_compute_image" "debian" {
  project = "debian-cloud"
  family  = "debian-12"
}

locals {
  startup = file("${path.module}/scripts/startup.sh")
}

# w1-vm in us-west1-b on subnetwork us-west-s1
resource "google_compute_instance" "w1_vm" {
  name         = "w1-vm"
  machine_type = "f1-micro"
  zone         = "us-west1-b"

  boot_disk {
    initialize_params { image = data.google_compute_image.debian.self_link }
  }

  network_interface {
    subnetwork = google_compute_subnetwork.us_west_s1.self_link
    access_config {}
  }

  metadata = { "startup-script" = local.startup }
}

# w2-vm in us-west1-b on subnetwork us-west-s2 with fixed internal IP
resource "google_compute_instance" "w2_vm" {
  name         = "w2-vm"
  machine_type = "f1-micro"
  zone         = "us-west1-b"

  boot_disk {
    initialize_params { image = data.google_compute_image.debian.self_link }
  }

  network_interface {
    subnetwork = google_compute_subnetwork.us_west_s2.self_link
    network_ip = "10.11.0.100"
    access_config {}
  }

  metadata = { "startup-script" = local.startup }
}

# e1-vm in us-east5-a
resource "google_compute_instance" "e1_vm" {
  name         = "e1-vm"
  machine_type = "e2-medium"
  zone         = "us-east5-a"

  boot_disk {
    initialize_params { image = data.google_compute_image.debian.self_link }
  }

  network_interface {
    subnetwork = google_compute_subnetwork.us_east5.self_link
    access_config {}
  }

  metadata = { "startup-script" = local.startup }
}

# eu1-vm in europe-west1-d
resource "google_compute_instance" "eu1_vm" {
  name         = "eu1-vm"
  machine_type = "f1-micro"
  zone         = "europe-west1-d"

  boot_disk {
    initialize_params { image = data.google_compute_image.debian.self_link }
  }

  network_interface {
    subnetwork = google_compute_subnetwork.europe_west1.self_link
    access_config {}
  }

  metadata = { "startup-script" = local.startup }
}

# asia1-vm in asia-east1-b
resource "google_compute_instance" "asia1_vm" {
  name         = "asia1-vm"
  machine_type = "f1-micro"
  zone         = "asia-east1-b"

  boot_disk {
    initialize_params { image = data.google_compute_image.debian.self_link }
  }

  network_interface {
    subnetwork = google_compute_subnetwork.asia_east1.self_link
    access_config {}
  }

  metadata = { "startup-script" = local.startup }
}
