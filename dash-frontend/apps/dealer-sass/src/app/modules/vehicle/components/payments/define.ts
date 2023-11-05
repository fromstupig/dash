export const DefaultVehicle = {
  msrp: 24020,
  vin: '1HGCV1F19LA029534'
};

export const LeasePayment = {
  default: {
    dueAtSigningAmount: 3000,
    term: 36,
    mileage: 12000
  },
  options: {
    mileage: [10000, 12000, 15000],
    term: [24, 36, 48]
  }
};

export const LoanPayment = {
  default: {
    downPayment: 3000,
    term: 60
  },
  options: {
    term: [48, 60, 72]
  }
}

export const DealType = {
  Cash: 'purchase',
  Lease: 'lease',
  Finance: 'loan'
};
