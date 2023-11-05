export interface Vehicle {
  id: number
  name: string
  manufacture_code: string
  galleries: any[]
  transmissions: any[]
  drive_trains: any[]
  standard_feature: object
  base_MSRP: number
}

export interface VehiclePaymentOptionBox {
  title: string
  description: string
}
