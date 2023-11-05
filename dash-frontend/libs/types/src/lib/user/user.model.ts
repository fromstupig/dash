export interface User {
  address?: string;
  avatarUrl?: string;
  email: string;
  facebookId?: string;
  fullName: string;
  googleId?: string;
  id?: number;
  password?: string;
  phoneNumber?: string;
  title?: string;
  type?: User.TypeEnum;
}
export namespace User {
  export type TypeEnum = 'HOST' | 'TENANT' | 'EXTERNAL';
  export const TypeEnum = {
    HOST: 'HOST' as TypeEnum,
    TENANT: 'TENANT' as TypeEnum,
    EXTERNAL: 'EXTERNAL' as TypeEnum
  };
}
