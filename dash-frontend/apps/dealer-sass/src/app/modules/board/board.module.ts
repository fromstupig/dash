import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientJsonpModule, HttpClientModule } from '@angular/common/http';
import { NzCollapseModule } from 'ng-zorro-antd/collapse';
import { NzModalModule } from 'ng-zorro-antd/modal';
import { NzSkeletonModule } from 'ng-zorro-antd/skeleton';
import { BoardComponent } from './pages/board/board.component';
import { BoardRoutingModule } from './board-routing.module';
import { RequestService } from './services/request.service';
import { NzTableModule } from 'ng-zorro-antd/table';

@NgModule({
  declarations: [BoardComponent],
  imports: [
    CommonModule,
    BoardRoutingModule,
    HttpClientModule,
    HttpClientJsonpModule,
    NzCollapseModule,
    NzModalModule,
    NzSkeletonModule,
    NzTableModule
  ],
  providers: [RequestService]
})
export class BoardModule {
}
